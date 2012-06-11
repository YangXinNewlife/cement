"""
Bit.ly Framework Extension Library.
        
"""

import re
import json
from urllib2 import urlopen
from cement2.core import meta, backend

Log = backend.minimal_logger(__name__)

class Bitly(meta.MetaMixin):
    """
    This class provides a mechanism for shortening long URLs using the Bit.ly
    API.
    
    Required Arguments:
    
        user
            The Bit.ly API User.
            
        apikey
            The Bit.ly API Key.
        
        baseurl
            The Bit.ly API Baseurl.
            
    Optional Arguments:
        
        enabled
            Whether or not to shorten URLs.  If False, the shorten() function
            will simply return the original URL.
        
    """
    class Meta:
        user = None
        apikey = None
        baseurl = 'https://api-ssl.bitly.com/v3/shorten/'
        enabled = True    
    
    def __init__(self, user, apikey, baseurl, **kw):
        kw['user'] = user
        kw['apikey'] = apikey
        kw['baseurl'] = baseurl
        super(Bitly, self).__init__(**kw)
        
        if not self._meta.user:
            Log.debug('Missing bitly user, disabling ext_bitly')
            self.enabled = False
        elif not self._meta.apikey:
            Log.debug('Missing bitly apikey, disabling ext_bitly')
            self.enabled = False
        elif not self._meta.baseurl:
            Log.debug('Missing bitly baseurl, disabling ext_bitly')
            self.enabled = False
            
    def shorten(self, long_url):
        """
        Takes a long URL and shortens it using Bit.ly.
        
        Required Arguments:
        
            long_url
                The URL to shorten.
                
        """
        if not self._meta.enabled:
            Log.debug('bit.ly shortening service is not enabled, skipping.')
            return long_url
            
        bitly_url = "%s?format=json&longUrl=%s&login=%s&apiKey=%s" % (
            self._meta.baseurl,
            unicode(long_url),
            self._meta.user,
            self._meta.apikey,
            )
        bitly_url = re.sub('\+', '%2b', bitly_url)
        res = urlopen(bitly_url)
        try:
            data = json.loads(res.read())
            url = data['data']['url']
            return url
        except TypeError, e:
            Log.debug("unable to shorten URL with bit.ly service! %s" % e.args[0])
            return long_url
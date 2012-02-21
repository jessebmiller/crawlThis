from django.http import HttpResponse
import random
import hashlib

def seedchain(seed, chain_length):
    """ generates a chain of hashes from seed having chain_length elements """
    for index in range(chain_length):
        seed = str(long(seed)*7 % 777777)
        yield seed

def build_crawlable_page(request, page_seed=1, abs_url=False):
    """ returns a page to return based on the page_seed """

    a = "<a href='%s' />%s</a>"
    p = "<p>%s</p>"
    
    num_links = long(page_seed) % 25 + 1

    html = p % ("this page has %s links" % num_links) 

    for seed in seedchain(page_seed, num_links):
        if abs_url:
            url = request.build_absolute_uri(seed)
        else:
            url = seed
        html += p % (a % (url, url))

    return html

def index(request):
    """
    random url's end up here. 

    this returns an outline of what url it was rendered from and the urls it points to 
    """    

    page_seed = random.getrandbits(32)
    html = build_crawlable_page(request, page_seed)

    return HttpResponse(html)
    
def test_get_page(request):
    """ returns a known explcit page """

    return HttpResponse( "pass" )

def crawl_test(request, page_seed):
    """ 
    provides the same pages for each link every time so we can ensure
    that a crawl produces the same result every time
    """
    
    return HttpResponse( page_seed + build_crawlable_page(request, page_seed) )

def abs_crawl_test(request, page_seed):
    """ 
    provides the same pages for each link every time so we can ensure
    that a crawl produces the same result every time

    uses absolute urls
    """
    
    return HttpResponse( page_seed + build_crawlable_page(request, page_seed, True) )
    

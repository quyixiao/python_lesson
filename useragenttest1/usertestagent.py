from user_agents import parse

useragents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0']

for ustring in useragents:
    ua = parse(ustring)
    print(ua.browser.family,ua.browser.version_string)

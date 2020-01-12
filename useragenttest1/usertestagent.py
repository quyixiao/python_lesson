from user_agents import parse

useragents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36']

for ustring in useragents:
    ua = parse(ustring)
    print(ua.browser.family,ua.browser.version_string)


if __name__ == '__main__':
    i = 1;
    str  = ""
    base_url = 'http://www.ireadweek.com/index.php/index/%s.html'
    while i <= 194:
        print(base_url %i)
        str = str+"'" + base_url % i+"', "
        print(str)
        i += 1

from bs4 import BeautifulSoup


filename = ''
with open(filename, 'r') as html_file: 
    content = html_file.read()
    print(content)

    # use beautifulsoup to prettify html file and work with tags like python objects 
    soup = BeautifulSoup(content, 'lxml')     # creating an instance of beautiful soup 
    print(soup.prettify)    # print html code in a more pretty way 

    # grab some specific information in html file 
    tags = soup.find('h5')    # return string, search for the first element and then stop 
    print(tags)

    courses_html_tags = soup.find_all('h5')    # find all h5 tags 
    for course in courses_html_tags: 
        print(course.text)   # return all the course that is available from that page 

    # grab the price for each course 
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards: 
        print(course.h5)

    for course in course_cards: 
        course_name = course.h5.text                # tag that responsible for course name 
        course_price = course.a.text.split()[-1]    # tag that responsible for course price 

        print(course_name)
        print(course_price)

        print(f'{course_name} costs {course_price}')























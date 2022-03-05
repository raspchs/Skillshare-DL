import sys, os
from skillshare import Skillshare, splash
#from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
#    dl = Skillshare(cookie)
    dl = Skillshare("PHPSESSID=391e9b154cb73f67c4cc15362238f5ce")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()

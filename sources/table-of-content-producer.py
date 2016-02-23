'''
    The script was wrote to generate table of content for a markdown article.
    Just need to copy the md file to same folder and execute the command:

    `python table-of-content-producer.py test.md`
    `python table-of-content-producer.py /Users/appledev072/Documents/projects-private/General-Resources-Box/md/development/guidance_how_git_been_used_in_projects.md`

    If you wanna more features function, you can refer to another https://github.com/thlorenz/doctoc.
'''
import sys, re

if len(sys.argv) == 2:
    fname = sys.argv[1]
    newlines = ''
    rootlevel = None

    with open(fname, 'r') as f:

        lines = f.readlines()

        for line in lines:
            result = re.match(r"\s*(\#+)\s+(.+)", line)
            if result:
                level = len(result.group(1))
                title = result.group(2)
                if rootlevel == None:
                    rootlevel = level
                print result.group(1) + ',' + str(level) + ',' + title
                id =  re.sub(r'\s+', '-', title.lower())
                id =  re.sub(r'[^\w^\-]+', '', id);

                newlines = newlines + (' ' * 4 * (level - rootlevel) + '- [' + title + '](#' + id + ')').rstrip('\r\n') + '\n'
        f.close()

    with open(fname, 'r+b') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(newlines + content)
        f.close()
else:
    print "Error: wrong parameters"
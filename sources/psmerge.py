import sys,xreadlines,os,thread,threading,config;
from magic import *;

def openpsfile(fname):
    try:
        fd=open(fname,'r');
    except IOError, (errno, strerror):
        print "Can\'t open file ",fname
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t open file ",fname;
        print "Unexpected error: ",sys.exc_info()[0]
        return -1;
    else:
        return fd;

def createpsfile(fname):
    try:
        fd=open(fname,'w');
    except IOError, (errno, strerror):
        print "Can\'t create file: ",fname
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t create file: ",fname;
        print "Unexpected error: ",sys.exc_info()[0]
        return -1;
    else:
        return fd;

def getpsbody(fd):
    #body2=[];
    body=[];
    try:
        body=fd.xreadlines();
    except IOError, (errno, strerror):
        print "Can\'t read ps-file: ",fd
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t read ps-file: ",fd
        print "Unexpected error: ",sys.exc_info()[0]
        return body;
    #    else:
    #        for line in body:
    #            if line[len(line)-2:]=='\r\n':
    #                body2.append(line[0:len(line)-2]);
    #            else:
    #                body2.append(line);
    else:
        return body;

def setkonicaoption(psbody,option,value):
    body2=[];
    beginffound=0;
    for line in psbody:
        if beginffound==1:
            if line==featureend+'\n':
                body2.append(line);
                beginffound=0
            else:
                continue;
        else:
            for feature in option:
                if line==featurebegin+option[feature]['name']+'\n':
                    beginffound=1;
                    body2.append(featurebegin+option[value]['name']+'\n');
                    body2.append(option[value]['cmd1']+'\n');
                    if option[value]['cmd2']!='':
                        body2.append(option[value]['cmd2']+'\n');
                    break;
            else:
                body2.append(line);
    return body2;

def makeDOScrlf(body):
    #    body2=[];
    #    for line in body:
    #        body2.append(line+'\r\n');
    #    return body2;
    return body;


def prepareps(fname):
    body=[];
    psfd=openpsfile(fname);
    if psfd!=-1:
        body=getpsbody(psfd);
        body=setkonicaoption(body,staple,config.outoptions['staple']);
        body=setkonicaoption(body,duplex,config.outoptions['duplex']);
        body=setkonicaoption(body,outtray,config.outoptions['outtray']);
        #body=makeDOScrlf(body);
        try:
            psfd.close();
        except IOError, (errno, strerror):
            print "Can\'t close file: ",psfd
            print "I/O error(%s): %s" % (errno, strerror)
        except:
            print "Can\'t close file: ",psfd
            print "Unexpected error: ",sys.exc_info()[0]
        try:
            os.remove(fname);
        except IOError, (errno, strerror):
            print "Can\'t remove file: ",fname
            print "I/O error(%s): %s" % (errno, strerror)
        except:
            print "Can\'t remove file: ",fname
            print "Unexpected error: ",sys.exc_info()[0]

    return body;

def prepareoutps(fd):
    try:
        fd.writelines(psprolog);
    except IOError, (errno, strerror):
        print "Can\'t write to file: ",fd
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t write to file: ",fd
        print "Unexpected error: ",sys.exc_info()[0]


def mergeps(fd,psbody):
    try:
        fd.write('_begin_job_\n')
        fd.writelines(psbody);
        fd.write('_end_job_\n')
    except IOError, (errno, strerror):
        print "Can\'t write to file: ",fd
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t write to file: ",fd
        print "Unexpected error: ",sys.exc_info()[0]

#########################################

if len(sys.argv)==1:
    print 'No source directory given';
    sys.exit();

outcache=[];
for ps in os.listdir(sys.argv[1]):
    outcache.append(prepareps(sys.argv[1]+ps));

outpsfd=createpsfile(config.outputps);
if outpsfd!=-1:
    prepareoutps(outpsfd);
    for psbody in outcache:
        mergeps(outpsfd,psbody);
    try:
        outpsfd.close();
    except IOError, (errno, strerror):
        print "Can\'t close file: ",outpsfd
        print "I/O error(%s): %s" % (errno, strerror)
    except:
        print "Can\'t close file: ",outpsfd
        print "Unexpected error: ",sys.exc_info()[0]

# будет глюк, если быстро пошлют на печать два раза или больше
# не забыть: удалять ps после чтения...или еще что-нибудь делать
# ускорить потом работу setk..option- чтобы по десять раз не проходил, а просто
#  сравнимал каждую строку
# если в директории есть поддиректории - трапается
# сделать все except и проверки
# всегда ли в оригинальном ps есть все опции ? если не будет, то и нашей не будет
# сделать все-таки threads --- быстрее будет

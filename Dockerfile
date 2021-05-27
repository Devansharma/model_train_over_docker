FROM centos:latest

RUN yum install python36 -y

RUN yum install python3-devel -y
    

RUN pip3 install pandas && \
    pip3 install scikit-learn

COPY salary.csv .

COPY model.py .

RUN python3 model.py 

CMD /bin/sh


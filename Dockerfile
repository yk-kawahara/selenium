FROM ubuntu:16.04

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt update && apt install -y wget
RUN apt upgrade -y
RUN apt install -y libgconf2-4
RUN apt install -y unzip
RUN apt install -y libx11-dev

WORKDIR /home/test
RUN apt install -y python3.6 python3.6-dev
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN pip3 install selenium
RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
ENV PATH $PATH:/home/test

WORKDIR /home/test
RUN apt install -y libnss3
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt update
RUN apt install -y google-chrome-stable
RUN pip install pyvirtualdisplay
RUN apt install -y xvfb

COPY web-get-ubuntu.py /home/test
COPY config.txt /home/test
RUN apt install fonts-ipafont-gothic fonts-ipafont-mincho



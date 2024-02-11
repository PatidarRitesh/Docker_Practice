from python

WORKDIR /myapp
COPY ./sqlDemo.py .

RUN pip install pymysql
RUN pip install cryptography

CMD [ "python", "sqlDemo.py"]
FROM python 

WORKDIR /myapp

COPY /doc.py .

#the line was imapliment the code 

RUN pip install requests  

CMD ["python" , "doc.py"]
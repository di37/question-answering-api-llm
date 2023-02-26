FROM python:3.10.8

WORKDIR /app

ENV PATH="${PATH}:/root/.cargo/bin"
RUN curl --proto '=https' --tlsv1.2 -o rust.sh -sSf https://sh.rustup.rs 
RUN chmod +x rust.sh;./rust.sh -y

RUN apt-get update
RUN apt-get install gcc g++ libsm6 libxext6 -y
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python", "-u", "main.py"]
FROM ramadhani892/ramagans:slim-buster

RUN git clone -b main https://ramadhani892/DEVEL /home/main/ \
WORKDIR /home/main/

CMD ["python3", "-m" "userbot"]

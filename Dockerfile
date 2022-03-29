FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b main https://github.com/ramadhani892/DEVEL /home/main/ \
    && chmod 777 /home/main \
    && mkdir /home/main/bin/
WORKDIR /home/main/


CMD ["python3", "-m", "userbot"]

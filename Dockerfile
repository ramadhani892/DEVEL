FROM ramadhani892/ramagans:slim-buster
# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b main https://github.com/ramadhani892/DEVEL home/devel/ 
WORKDIR /home/devel
CMD ["python3", "-m", "userbot"]

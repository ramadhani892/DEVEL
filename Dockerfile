FROM ramadhani892/ramagans:slim-buster

# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
##

RUN git clone -b master https://github.com/ramadhani892/RAM-UBOT home/ramagans/
CMD ["python3", "-m", "userbot"]
WORKDIR home/ramagans/

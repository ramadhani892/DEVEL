FROM ramadhani892/ramagans:slim-buster
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b RAM-UBOT https://github.com/ramadhani892/DEVEL /home/ramagans/
WORKDIR /home/ramagans/
CMD ["python3", "-m", "userbot"]

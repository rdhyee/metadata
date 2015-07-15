set -e
docker build -t rdhyee/metadata .
DOCUMENT_DIR=${1:-`pwd`}
docker run -it  -v $DOCUMENT_DIR:/data/  rdhyee/metadata bash

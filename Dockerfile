FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src .

RUN mkdir -p /tb_logs
VOLUME /tb_logs

ENV LEARNING_RATE=4e-05
ENV BATCH_SIZE=32
ENV WEIGHT_DECAY=0.1
ENV WARMUP_STEPS=50
ENV DROPOUT_RATE=0.6

CMD python train.py --learning_rate $LEARNING_RATE --batch_size $BATCH_SIZE --weight_decay $WEIGHT_DECAY --warmup_steps $WARMUP_STEPS --dropout_rate $DROPOUT_RATE
#!/usr/bin/env bash
python3 utils/train_model.py -t squad \
                         -m deeppavlov.agents.squad.squad:SquadAgent \
                         --batchsize 64 \
                         --display-examples False \
                         --max-train-time -1 \
                         --num-epochs -1 \
                         --log-every-n-secs 60 \
                         --log-every-n-epochs -1 \
                         --validation-every-n-secs 1800 \
                         --validation-every-n-epochs -1 \
                         --chosen-metric f1 \
                         --validation-patience 5 \
                         --lr-drop-patience 1 \
                         --type 'fastqa_default' \
                         --lr 0.001 \
                         --lr_drop 0.3 \
                         --linear_dropout 0.0 \
                         --embedding_dropout 0.3 \
                         --rnn_dropout 0.0 \
                         --recurrent_dropout 0.0 \
                         --input_dropout 0.0 \
                         --output_dropout 0.0 \
                         --context_enc_layers 1 \
                         --question_enc_layers 1 \
                         --encoder_hidden_dim 300 \
                         --projection_dim 300 \
                         --pointer_dim 300 \
                         --model-file '../save/squad/squad_fastqa_e/squad1' \
                         --embedding_file '../embeddings/glove.840B.300d.txt'
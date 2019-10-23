#!/usr/bin/env bash
source activate tensorflow-gpu
export CUDA_VISIBLE_DEVICES=6
python tornado_server.py &

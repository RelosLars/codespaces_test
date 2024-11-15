import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training.")
    parser.add_argument("--learning_rate", type=float, default=1e-3, help="Learning rate for the optimizer.")
    parser.add_argument("--weight_decay", type=float, default=0.1, help="Weight decay for the optimizer.")
    parser.add_argument("--warmup_steps", type=int, default=0, help="Number of warmup steps for the scheduler.")
    parser.add_argument("--dropout_rate", type=float, default=0.1, help="Dropout rate for regularization.")
    return parser.parse_args()

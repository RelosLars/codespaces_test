from lightning.pytorch.loggers import TensorBoardLogger

def get_tensorboard_logger(args):
    run_name = (f"LR={args.learning_rate}_"
                f"BS={args.batch_size}_"
                f"WD={args.weight_decay}_"
                f"WS={args.warmup_steps}_"
                f"DR={args.dropout_rate}")

    return TensorBoardLogger("tb_logs", name=run_name)

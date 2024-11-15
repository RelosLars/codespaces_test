from data_modules.GLUEDataModule import GLUEDataModule
from models.GLUETransformer import GLUETransformer
from utils.config import parse_args
from utils.logger import get_tensorboard_logger
import lightning as L

if __name__ == "__main__":
    args = parse_args()

    # Initialize TensorBoard logger
    logger = get_tensorboard_logger(args)

    # Print Hyperparameters
    print("Hyperparameters configuration:")
    for param, value in vars(args).items():
        print(f"{param}: {value}")

    # Set random seed for reproducibility
    L.seed_everything(42)

    # Initialize the data module with args
    dm = GLUEDataModule(
        model_name_or_path="distilbert-base-uncased",
        task_name="mrpc",
        max_seq_length=128,
        train_batch_size=args.batch_size,
        eval_batch_size=args.batch_size
    )

    dm.setup("fit")

    # Initialize the model with args, including new hyperparameters
    model = GLUETransformer(
        model_name_or_path="distilbert-base-uncased",
        num_labels=dm.num_labels,
        task_name=dm.task_name,
        learning_rate=args.learning_rate,
        weight_decay=args.weight_decay,
        warmup_steps=args.warmup_steps,
        dropout_rate=args.dropout_rate
    )

    # Setup and run the trainer
    trainer = L.Trainer(
        max_epochs=3,
        accelerator="auto",
        devices=1,
        logger=logger,
    )

    # Start the model training
    trainer.fit(model, datamodule=dm)

import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. 
    By default it gives an embedding of the Wikipedia Chameleons dataset.
    The default hyperparameters give a good quality representation without grid search.
    Representations are sorted by ID.
    """
    parser = argparse.ArgumentParser(description = "Run MUSAE/AE.")

    parser.add_argument('--graph-input',
                        nargs = '?',
                        default = "./input/edges/chameleon_edges.csv",
	                help = 'Input edge list csv.')

    parser.add_argument('--features-input',
                        nargs = '?',
                        default = "./input/features/chameleon_features.json",
	                help = 'Input features json.')

    parser.add_argument('--output',
                        nargs = '?',
                        default = './output/chameleon_embedding.csv',
	                help = 'Embeddings path.')

    parser.add_argument('--log',
                        nargs = '?',
                        default = './logs/chameleon.json',
	                help = 'log  path.')

    parser.add_argument('--dimensions',
                        type = int,
                        default = 24,
	                help = 'Number of dimensions. Default is 32.')

    parser.add_argument('--walk-number',
                        type = int,
                        default = 5,
	                help = 'Number of walks. Default is 5.')

    parser.add_argument('--walk-length',
                        type = int,
                        default = 80,
	                help = 'Walk length. Default is 80.')

    parser.add_argument('--base-model',
                        nargs = '?',
                        default = 'null',
	                help = 'Random walk order.')

    parser.add_argument('--model',
                        nargs = '?',
                        default = 'musae',
	                help = 'Random walk order.')

    parser.add_argument('--sampling',
                        nargs = '?',
                        default = 'first',
	                help = 'Random walk order.')

    parser.add_argument('--P',
                        type = float,
                        default = 1.0,
	                help = 'Number of walks. Default is 1.0.')

    parser.add_argument('--Q',
                        type = float,
                        default = 1.0,
	                help = 'Number of walks. Default is 1.0.')

    parser.add_argument('--down-sampling',
                        type = float,
                        default = 0.001,
	                help = 'Number of walks. Default is 0.001.')

    parser.add_argument('--exponent',
                        type = float,
                        default = 0.75,
	                help = 'Number of walks. Default is 0.001.')

    parser.add_argument('--alpha',
                        type = float,
                        default = 0.05,
	                help = 'Number of walks. Default is 0.05.')

    parser.add_argument('--min_alpha',
                        type = float,
                        default = 0.025,
	                help = 'Number of walks. Default is 0.025.')

    parser.add_argument('--approximation-order',
                        type = int,
                        default = 3,
	                help = 'Number of neighbor embeddings. Default is 3.')

    parser.add_argument('--min-count',
                        type = int,
                        default = 1,
	                help = 'Number of neighbor embeddings. Default is 3.')

    parser.add_argument('--negative-samples',
                        type = int,
                        default = 5,
	                help = 'Number of neighbor embeddings. Default is 5.')

    parser.add_argument('--workers',
                        type = int,
                        default = 4,
	                help = 'Number of cores. Default is 4.')

    parser.add_argument('--epochs',
                        type = int,
                        default = 5,
	                help = 'Number of epochs. Default is 5.')

    return parser.parse_args()


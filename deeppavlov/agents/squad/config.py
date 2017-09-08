import os
import sys
import logging

def add_cmdline_args(parser):
    # Runtime environment
    agent = parser.add_argument_group('Paraphraser Arguments')
    agent.add_argument('--random_seed', type=int, default=1013)

    # Basics
    agent.add_argument('--pretrained_model', type=str, default=None,
                       help='Load dict/features/weights/opts from this file prefix')

    # Model details

    # Predictions
    agent.add_argument('--answ_maxlen', type=int, default=15,
                       help='Maximum answer length')

    # Optimizer
    agent.add_argument('--optimizer', type=str, default='Adamax',
                        help='Optimizer to use')
    agent.add_argument('--grad_norm_clip', type=float, default=10.0,
                        help='Gradient norm clipping')
    agent.add_argument('--exp_decay', type=float, default=0.0,
                       help='Decay in learning rate after each iteration')
    agent.add_argument('--lr', type=float, default=0.0005,
                       help='Initial learning rate')
    agent.add_argument('--lr_drop', type=float, default=0.5,
                       help='Decrease learning rate if validation F1 score is not dropping')
    agent.add_argument('--lr_drop_patience', type=int, default=1,
                       help='How much epochs to wait before decreasing learning rate')

    # Word embeddings
    agent.add_argument('--word_embedding_dim', type=int, default=300,
                        help='Word embedding dimension')

    # Context and question embeddings
    agent.add_argument('--context_embedding_dim', type=int, default=308,
                        help='Shape of context token vector')
    agent.add_argument('--question_embedding_dim', type=int, default=300,
                        help='Shape of question token vector')

    # Char embeddings
    agent.add_argument('--char_embedding_dim', type=int, default=32,
                        help='Char embedding vector shape')

    # Aligned question representation
    agent.add_argument('--aligned_question_dim', type=int, default=300,
                        help='Inner dim in aligned question layer')

    # Encoder
    agent.add_argument('--encoder_hidden_dim', type=int, default=128,
                        help='Hidden dimension of encoder')
    agent.add_argument('--question_enc_layers', type=int, default=3,
                        help='Number of layers in question encoder')
    agent.add_argument('--context_enc_layers', type=int, default=3,
                        help='Number of layers in context encoder')

    # Projection
    agent.add_argument('--projection_dim', type=int, default=128,
                        help='Number of layers in context encoder')

    # Start end poiners
    agent.add_argument('--pointer_dim', type=int, default=128,
                        help='Number of layers in context encoder')

    # Dropout settings
    agent.add_argument('--embedding_dropout', type=float, default=0.5)
    agent.add_argument('--linear_dropout', type=float, default=0.25)
    agent.add_argument('--rnn_dropout', type=float, default=0.25)
    agent.add_argument('--recurrent_dropout', type=float, default=0.25)


    # Basics
    agent.add_argument('--embedding_file', type=str, default=None,
                        help='File of space separated embeddings: w e1 ... ed')

    # Additional features
    agent.add_argument('--use_in_question', type='bool', default=True,
                        help='Whether to use in_question features')
    agent.add_argument('--use_tf', type='bool', default=True,
                        help='Whether to use tf features')
    agent.add_argument('--use_time', type=int, default=5,
                        help='Time features marking how recent word was said')


def set_defaults(opt):
    # Embeddings options
    if opt.get('embedding_file'):
        if not os.path.isfile(opt['embedding_file']):
            raise IOError('No such file: %s' % opt['embedding_file'])
        with open(opt['embedding_file']) as f:
            dim = len(f.readline().strip().split(' ')) - 1
        opt['embedding_dim'] = dim
    elif not opt.get('embedding_dim'):
        raise RuntimeError(('Either embedding_file or embedding_dim '
                            'needs to be specified.'))

def override_args(opt, override_opt):
    # Major model args are reset to the values in override_opt.
    # Non-architecture args (like dropout) are kept.
    args = set(['embedding_file', 'embedding_dim', 'hidden_size', 'doc_layers',
                'question_layers', 'rnn_type', 'optimizer', 'concat_rnn_layers',
                'question_merge', 'use_qemb', 'use_in_question', 'use_tf',
                'vocab_size', 'num_features', 'use_time'])
    for k, v in override_opt.items():
        if k in args:
            opt[k] = v


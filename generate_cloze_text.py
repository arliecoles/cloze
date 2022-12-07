#!/usr/bin/env python3

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Anki cloze text.')
    parser.add_argument('in_path', type=str, help='Path to input file, one phrase per line.')
    parser.add_argument('out_path', type=str, help='Path to output cloze file.')
    args = parser.parse_args()

    # Read in input file
    with open(args.in_path, 'r') as fp:
        in_lines = [x.strip() for x in fp.readlines()]
    print('Read {0}'.format(args.in_path))
    
    # Format
    print('Formatting...')
    out_lines = []
    for line in in_lines:
        words = line.split()
        out_words = ['{{{{c{0}::{1}}}}}'.format(i + 1, word) for i, word in enumerate(words)]
        # Ensure any punctuation is outside the brackets
        terminal_punct = '.,;:?!'
        for punct in terminal_punct:
            out_words = [word.replace('{0}}}}}'.format(punct), '}}}}{0}'.format(punct)) for word in out_words]
        out_line = ' '.join(out_words)
        out_lines.append(out_line)
        print('\t' + out_line)
    
    # Write to output file
    with open(args.out_path, 'w') as fp:
        for line in out_lines:
            fp.write('{0}\n'.format(line))
    print('Wrote {0}'.format(args.out_path))
    print('Done.')
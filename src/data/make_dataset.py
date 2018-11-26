# use Go IEX's pcap2json examples below
# pcap2csv parses out just open, high, low, close, volume by symbol w ns timestamp
pcap2csv < data%2Ffeeds%2F20180913%2F20180913_IEXTP1_DEEP1.0.pcap > 20180913_IEXTP1_DEEP1.0.csv
# pcap2json parses out the tcp headers and leave all of other message Database
pcap2json < data%2Ffeeds%2F20180913%2F20180913_IEXTP1_DEEP1.0.pcap > 20180913_IEXTP1_DEEP1.0.json

# json2parquet python library convert the json to parquet, which pandas and pyarrow work better with
from json2parquet import convert_json
# Infer Schema (requires reading dataset for column names)
convert_json('20180913_IEXTP1_DEEP1.0.json', '20180913_IEXTP1_DEEP1.0.parquet')


# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()

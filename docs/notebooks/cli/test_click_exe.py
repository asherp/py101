
import click 

@click.command()
@click.argument('integers', nargs = -1, type = int)
@click.option('--sum', 'accumulate', default=False, is_flag = True, 
    help='Whether to sum over inputs (default is max)')
def main(integers, accumulate):
    if accumulate:
        print(sum(integers))
    else:
        print(max(integers))

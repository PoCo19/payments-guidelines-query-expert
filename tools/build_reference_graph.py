"""Build an inactive, source-anchored corpus reference graph without embeddings."""
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from reference_graph import build_release
from tools.document_pipeline import write,read

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir',type=Path)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--previous',type=Path)
    a=p.parse_args()
    directory=a.data_dir or Path(read(ROOT/'config.json')['data_dir'])
    if a.output.exists():raise SystemExit('Output already exists; choose a new versioned path.')
    graph=build_release(directory,a.previous)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    write(a.output,graph)
    print(json.dumps(graph['summary']),a.output)

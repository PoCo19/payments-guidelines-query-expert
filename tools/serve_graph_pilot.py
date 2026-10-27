"""Launch an isolated graph-enabled preview using a copy of the normal configuration."""
import argparse
from pathlib import Path
import json
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import app


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,default=app.default_config_path())
    parser.add_argument('--port',type=int,default=8769)
    parser.add_argument('--graph',default='pilot/upi_extended_graph_v3.json')
    args=parser.parse_args()
    config=app.read_json(args.config)
    config['evidence_graph_path']=args.graph
    path=ROOT/'tmp/graph-pilot-config.json';path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
    print('Graph pilot: selected UPI amendment families and IPO limits. Independent source review pending.',flush=True)
    print('Use Related context. Strict searches and selected-document summaries/comparisons retain their existing behaviour.',flush=True)
    sys.argv=['app.py','serve','--config',str(path),'--port',str(args.port)]
    app.main()


if __name__=='__main__':main()

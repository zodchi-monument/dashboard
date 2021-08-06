from app import app, objects_dict
import glob
import yaml
from layouts import get_layout


if __name__ == "__main__":
    for g in glob.glob("./init_files/*.yaml"):
        with open(g, "r") as f:
            plant, agg = g.split("/")[-1].split(".")[0].split("_")
            if plant not in objects_dict.keys():
                objects_dict[plant] = {}
            objects_dict[plant][agg] = {}
            conf = yaml.load(f.read())
            for k in conf:
                objects_dict[plant][agg][k] = conf[k]["tags"]["input"]
    app.layout = get_layout(objects_dict)

    app.run_server(debug=True)
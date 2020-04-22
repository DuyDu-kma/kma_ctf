import "./main";
import $ from "jquery";
import KMActf from "../KMActf";
import Plotly from "plotly.js-basic-dist";
import Moment from "moment";
import { htmlEntities, cumulativeSum, colorHash } from "../utils";

const graph = $("#score-graph");
const table = $("#scoreboard tbody");
const config = {
  displaylogo: false,
  responsive: true
};
const layout = {
  title: "Top 10 Teams",
  paper_bgcolor: "rgba(0,0,0,0)",
  plot_bgcolor: "rgba(0,0,0,0)",
  hovermode: "closest",
  xaxis: {
    showgrid: false,
    showspikes: true
  },
  yaxis: {
    showgrid: false,
    showspikes: true
  },
  legend: {
    orientation: "h"
  }
};

const updateScores = () => {
  KMActf.api.get_scoreboard_list().then(response => {
    const teams = response.data;
    table.empty();

    for (let i = 0; i < teams.length; i++) {
      const row = [
        "<tr>",
        '<th scope="row" class="text-center">',
        i + 1,
        "</th>",
        '<td><a href="{0}/team/{1}">'.format(
          KMActf.config.urlRoot,
          teams[i].account_id
        ),
        htmlEntities(teams[i].name),
        "</a></td>",
        "<td>",
        teams[i].score,
        "</td>",
        "</tr>"
      ].join("");
      table.append(row);
    }
  });
};

const createGraph = () => {
  KMActf.api.get_scoreboard_detail({ count: 10 }).then(response => {
    const places = response.data;

    const teams = Object.keys(places);
    const traces = [];
    if (teams.length === 0) {
      // Replace spinner
      graph.html(
        '<div class="text-center"><h3 class="spinner-error">No solves yet</h3></div>'
      );
      return;
    }
    for (let i = 0; i < teams.length; i++) {
      const team_score = [];
      const times = [];
      for (let j = 0; j < places[teams[i]]["solves"].length; j++) {
        team_score.push(places[teams[i]]["solves"][j].value);
        const date = Moment(places[teams[i]]["solves"][j].date);
        times.push(date.toDate());
      }
      const trace = {
        x: times,
        y: cumulativeSum(team_score),
        mode: "lines+markers",
        name: places[teams[i]]["name"],
        marker: {
          color: colorHash(places[teams[i]]["name"] + places[teams[i]]["id"])
        },
        line: {
          color: colorHash(places[teams[i]]["name"] + places[teams[i]]["id"])
        }
      };
      traces.push(trace);
    }

    traces.sort((a, b) => {
      const score_diff = b["y"][b["y"].length - 1] - a["y"][a["y"].length - 1];
      if (!score_diff) {
        return a["x"][a["x"].length - 1] - b["x"][b["x"].length - 1];
      }
      return score_diff;
    });

    graph.empty(); // Remove spinners
    graph[0].fn = "KMActf_scoreboard_" + new Date().toISOString().slice(0, 19);
    Plotly.newPlot(graph[0], traces, layout, config);
  });
};

const updateGraph = () => {
  KMActf.api.get_scoreboard_detail({ count: 10 }).then(response => {
    const places = response.data;

    const teams = Object.keys(places);
    const traces = [];
    if (teams.length === 0) {
      return;
    }
    for (let i = 0; i < teams.length; i++) {
      const team_score = [];
      const times = [];
      for (let j = 0; j < places[teams[i]]["solves"].length; j++) {
        team_score.push(places[teams[i]]["solves"][j].value);
        const date = Moment(places[teams[i]]["solves"][j].date);
        times.push(date.toDate());
      }
      const trace = {
        x: times,
        y: cumulativeSum(team_score),
        mode: "lines+markers",
        name: places[teams[i]]["name"],
        marker: {
          color: colorHash(places[teams[i]]["name"] + places[teams[i]]["id"])
        },
        line: {
          color: colorHash(places[teams[i]]["name"] + places[teams[i]]["id"])
        }
      };
      traces.push(trace);
    }

    traces.sort((a, b) => {
      const score_diff = b["y"][b["y"].length - 1] - a["y"][a["y"].length - 1];
      if (!score_diff) {
        return a["x"][a["x"].length - 1] - b["x"][b["x"].length - 1];
      }
      return score_diff;
    });

    Plotly.react(graph[0], traces, layout, config);
  });
};

function update() {
  updateScores();
  updateGraph();
}

$(() => {
  setInterval(update, 300000); // Update scores every 5 minutes
  createGraph();
  updateGraph();
});

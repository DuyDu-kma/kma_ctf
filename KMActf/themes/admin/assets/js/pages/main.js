import KMActf from "core/KMActf";
import $ from "jquery";
import Moment from "moment";
import nunjucks from "nunjucks";
import { Howl } from "howler";
import events from "core/events";
import times from "core/times";
import styles from "../styles";
import { default as helpers } from "core/helpers";

KMActf.init(window.init);
window.KMActf = KMActf;
window.helpers = helpers;
window.$ = $;
window.Moment = Moment;
window.nunjucks = nunjucks;
window.Howl = Howl;

$(() => {
  styles();
  times();
  events(KMActf.config.urlRoot);
});

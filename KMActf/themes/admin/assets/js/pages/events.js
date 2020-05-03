import $ from "jquery";
import events from "core/events";
import KMActf from "core/KMActf";

$(() => {
  events(KMActf.config.urlRoot);
});

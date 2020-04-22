import "./main";
import KMActf from "core/KMActf";
import $ from "jquery";

const api_func = {
  users: (x, y) => KMActf.api.patch_user_public({ userId: x }, y),
  teams: (x, y) => KMActf.api.patch_team_public({ teamId: x }, y)
};

function toggleAccount() {
  const $btn = $(this);
  const id = $btn.data("account-id");
  const state = $btn.data("state");
  let hidden = undefined;
  if (state === "visible") {
    hidden = true;
  } else if (state === "hidden") {
    hidden = false;
  }

  const params = {
    hidden: hidden
  };

  api_func[KMActf.config.userMode](id, params).then(response => {
    if (response.success) {
      if (hidden) {
        $btn.data("state", "hidden");
        $btn.addClass("btn-danger").removeClass("btn-success");
        $btn.text("Hidden");
      } else {
        $btn.data("state", "visible");
        $btn.addClass("btn-success").removeClass("btn-danger");
        $btn.text("Visible");
      }
    }
  });
}

$(() => {
  $(".scoreboard-toggle").click(toggleAccount);
});

KMActf._internal.challenge.data = undefined

KMActf._internal.challenge.renderer = KMActf.lib.markdown();


KMActf._internal.challenge.preRender = function () { }

KMActf._internal.challenge.render = function (markdown) {
    return KMActf._internal.challenge.renderer.render(markdown)
}


KMActf._internal.challenge.postRender = function () { }


KMActf._internal.challenge.submit = function (preview) {
    var challenge_id = parseInt(KMActf.lib.$('#challenge-id').val())
    var submission = KMActf.lib.$('#submission-input').val()

    var body = {
        'challenge_id': challenge_id,
        'submission': submission,
    }
    var params = {}
    if (preview) {
        params['preview'] = true
    }

    return KMActf.api.post_challenge_attempt(params, body).then(function (response) {
        if (response.status === 429) {
            // User was ratelimited but process response
            return response
        }
        if (response.status === 403) {
            // User is not logged in or CTF is paused.
            return response
        }
        return response
    })
};

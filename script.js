fetch("/analyze", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        resume: resume,
        job_description: job
    })
});

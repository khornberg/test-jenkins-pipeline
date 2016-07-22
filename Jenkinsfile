stage 'Clone repo'
node {
    git poll: false, url: 'https://github.com/khornberg/test-jenkins-pipeline', branch: 'feature/longer-times'
}

stage 'Install deps'
node {
    sh 'virtualenv venv'
    sh '. venv/bin/activate'
    sh 'pip install django'
    stash includes: '**', name: 'repo'
}

stage 'Run Tests'
def branches = [:]
branches["one"] = {
    node {
        unstash 'repo'
        sh './manage.py test app1'
    }
}
branches["two"] = {
    node {
        unstash 'repo'
        sh './manage.py test app2'
    }
}
parallel branches

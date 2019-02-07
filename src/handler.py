import os

def run(event, context):
    project_id = os.environ.get("ProjectID")

    print('%s invoked' % project_id)

    if event and event.get('should_fail') is True:
        raise Exception('Failed on purpose')

    return 'Done'
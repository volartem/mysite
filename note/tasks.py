from celery import shared_task
import logging
from note.models import Something

logger = logging.getLogger('ip_logger')


@shared_task
def background_logging(obj):
    if not obj.get('path').startswith('/admin'):
        new_record = Something(status_code=int(obj.get('status_code')), method=obj.get('method'), ip=obj.get('ip'),
                               refer=obj.get('refer'), path=obj.get('path'))
        new_record.save()
    else:
        logger.warning("%s ===> %s" % (obj.get('path'), obj))

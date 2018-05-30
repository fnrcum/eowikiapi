from . import *


class ImagesModel(RethinkDBModel):
    _table = 'images'
    _pk = 'id'

    @classmethod
    def create(cls, args):
        post_args = args
        if not ("name" and "item_id") in post_args:
            return {"status": HTTPStatus.BAD_REQUEST,
                    "message": "Invalid request params, Accepted: 'name', 'item_id', "}, HTTPStatus.BAD_REQUEST
        for key, value in post_args.items():
            if value is None or value is "":
                return {"status": HTTPStatus.BAD_REQUEST,
                        "message": "Invalid request params: {0} has no value}".format(key)}, HTTPStatus.BAD_REQUEST
        with pool.get_resource() as res:
            r.table(cls._table).insert(post_args).run(res.conn)


class PagesModel(RethinkDBModel):
    _table = 'pages'
    _pk = 'id'

    @classmethod
    def create(cls, **kwargs):
        page_name = kwargs.get('page_name')
        page_title = kwargs.get('page_title')
        description = kwargs.get('description')
        accepted = kwargs.get('accepted')
        doc = {
            'page_name': page_name,
            'page_title': page_title,
            'description': description,
            'accepted': accepted,
            'date_created': datetime.now(r.make_timezone('+02:00')),
            'date_modified': datetime.now(r.make_timezone('+02:00'))
        }
        with pool.get_resource() as res:
            r.table(cls._table).insert(doc).run(res.conn)


class ItemsModel(RethinkDBModel):
    _table = 'items'
    _pk = 'id'

    @classmethod
    def create(cls, **kwargs):
        item_name = kwargs.get('item_name')
        description = kwargs.get('description')
        player_class = kwargs.get('player_class')
        item_type = kwargs.get('item_type')
        item_stats = kwargs.get('item_stats')
        doc = {
            'item_name': item_name,
            'description': description,
            'player_class': player_class,
            'item_type': item_type,
            'item_stats': item_stats,
            'date_created': datetime.now(r.make_timezone('+02:00')),
            'date_modified': datetime.now(r.make_timezone('+02:00'))
        }
        with pool.get_resource() as res:
            r.table(cls._table).insert(doc).run(res.conn)


class SkillsModel(RethinkDBModel):
    _table = 'skills'
    _pk = 'id'

    @classmethod
    def create(cls, **kwargs):
        skill_name = kwargs.get('skill_name')
        description = kwargs.get('description')
        skill_class = kwargs.get('skill_class')
        skill_type = kwargs.get('skill_type')
        skill_stats = kwargs.get('skill_stats')
        doc = {
            'skill_name': skill_name,
            'description': description,
            'skill_class': skill_class,
            'skill_type': skill_type,
            'skill_stats': skill_stats,
            'date_created': datetime.now(r.make_timezone('+02:00')),
            'date_modified': datetime.now(r.make_timezone('+02:00'))
        }
        with pool.get_resource() as res:
            r.table(cls._table).insert(doc).run(res.conn)


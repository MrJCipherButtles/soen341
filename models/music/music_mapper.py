from models.item.item_mapper import ItemMapper
from models.loanable.loanable_mapper import LoanableMapper


class MusicMapper(ItemMapper, LoanableMapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

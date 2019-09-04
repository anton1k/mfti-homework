import util
import search
import binary_search
import interpolation_search
# сравнение поисков
util.plot_search_results_small(
    ('Линейный поиск', search.search),
    ('Бинарный поиск', binary_search.binary_search),
    ('Интерполяционный поиск', interpolation_search.interpolation_search),
)
util.plot_search_results_huge(
    ('Бинарный поиск', binary_search.binary_search),
    ('Интерполяционный поиск', interpolation_search.interpolation_search),
)
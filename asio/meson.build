project('asio', 'cpp',
    default_options : [
        'cpp_std=c++17'
    ]
)

boost_dep = dependency(
    'boost',
    modules : [
        'thread',
        'system',
        'chrono'
    ]
)

executable('asio',
    'main.cpp',
    dependencies : [
        boost_dep,
    ]
)

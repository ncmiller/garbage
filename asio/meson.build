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

executable('daytime_client',
    'daytime_client.cpp',
    dependencies : [
        boost_dep,
    ]
)

executable('daytime_server',
    'daytime_server.cpp',
    dependencies : [
        boost_dep,
    ]
)

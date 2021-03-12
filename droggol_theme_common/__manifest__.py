# -*- coding: utf-8 -*-
# Copyright (c) 2019-Present Droggol. (<https://www.droggol.com/>)

{
    'name': 'Droggol Theme Common',
    'description': 'Droggol Theme Common',
    'category': 'eCommerce',
    'version': '13.0.0.8.1',
    'depends': [
        'website_theme_install',
        'sale_product_configurator',
        'website_sale_comparison',
        'website_sale_wishlist',
        'website_sale_stock',
    ],

    'license': 'OPL-1',
    'author': 'Droggol',
    'company': 'Droggol',
    'maintainer': 'Droggol',
    'website': 'https://www.droggol.com/',

    "price": 15.00,
    "currency": "USD",
    "live_test_url": "https://prime-fashion-1.droggol.com/",

    'data': [
        'security/ir.model.access.csv',
        'data/snippet_images.xml',
        'data/groups.xml',
        'views/assets.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/variant_templates.xml',
        'views/svg_images.xml',
        'views/res_config_settings_views.xml',
        # Snippets
        'views/snippets/s_animation_block_1.xml',
        'views/snippets/s_animation_block_2.xml',
        'views/snippets/s_banner_1.xml',
        'views/snippets/s_banner_2.xml',
        'views/snippets/s_banner_3.xml',
        'views/snippets/s_banner_4.xml',
        'views/snippets/s_banner_5.xml',
        'views/snippets/s_banner_6.xml',
        'views/snippets/s_banner_7.xml',
        'views/snippets/s_banner_8.xml',
        'views/snippets/s_banner_9.xml',
        'views/snippets/s_banner_10.xml',
        'views/snippets/s_banner_11.xml',
        'views/snippets/s_banner_12.xml',
        'views/snippets/s_banner_13.xml',
        'views/snippets/s_call_to_action_1.xml',
        'views/snippets/s_call_to_action_2.xml',
        'views/snippets/s_call_to_action_3.xml',
        'views/snippets/s_call_to_action_4.xml',
        'views/snippets/s_call_to_action_5.xml',
        'views/snippets/s_category_1.xml',
        'views/snippets/s_category_2.xml',
        'views/snippets/s_category_3.xml',
        'views/snippets/s_category_4.xml',
        'views/snippets/s_clients_1.xml',
        'views/snippets/s_clients_2.xml',
        'views/snippets/s_clients_3.xml',
        'views/snippets/s_clients_4.xml',
        'views/snippets/s_coming_soon_1.xml',
        'views/snippets/s_coming_soon_2.xml',
        'views/snippets/s_countdown_1.xml',
        'views/snippets/s_countdown_2.xml',
        'views/snippets/s_countdown_3.xml',
        'views/snippets/s_countdown_4.xml',
        'views/snippets/s_counters_1.xml',
        'views/snippets/s_counters_2.xml',
        'views/snippets/s_counters_3.xml',
        'views/snippets/s_counters_4.xml',
        'views/snippets/s_counters_5.xml',
        'views/snippets/s_cover_1.xml',
        'views/snippets/s_cover_2.xml',
        'views/snippets/s_cover_3.xml',
        'views/snippets/s_cover_4.xml',
        'views/snippets/s_cover_5.xml',
        'views/snippets/s_gallery_1.xml',
        'views/snippets/s_gallery_2.xml',
        'views/snippets/s_gallery_3.xml',
        'views/snippets/s_gallery_4.xml',
        'views/snippets/s_gallery_5.xml',
        'views/snippets/s_heading_1.xml',
        'views/snippets/s_heading_2.xml',
        'views/snippets/s_heading_3.xml',
        'views/snippets/s_heading_4.xml',
        'views/snippets/s_heading_5.xml',
        'views/snippets/s_icon_block_1.xml',
        'views/snippets/s_icon_block_2.xml',
        'views/snippets/s_icon_block_3.xml',
        'views/snippets/s_icon_block_4.xml',
        'views/snippets/s_icon_block_5.xml',
        'views/snippets/s_icon_block_6.xml',
        'views/snippets/s_icon_block_7.xml',
        'views/snippets/s_icon_block_8.xml',
        'views/snippets/s_icon_block_9.xml',
        'views/snippets/s_icon_block_10.xml',
        'views/snippets/s_icon_block_11.xml',
        'views/snippets/s_icon_block_12.xml',
        'views/snippets/s_info_block_1.xml',
        'views/snippets/s_info_block_2.xml',
        'views/snippets/s_info_block_3.xml',
        'views/snippets/s_info_block_4.xml',
        'views/snippets/s_info_block_5.xml',
        'views/snippets/s_info_block_6.xml',
        'views/snippets/s_offer_1.xml',
        'views/snippets/s_offer_2.xml',
        'views/snippets/s_offer_3.xml',
        'views/snippets/s_offer_4.xml',
        'views/snippets/s_pricing_1.xml',
        'views/snippets/s_pricing_2.xml',
        'views/snippets/s_pricing_3.xml',
        'views/snippets/s_pricing_4.xml',
        'views/snippets/s_pricing_5.xml',
        'views/snippets/s_pricing_6.xml',
        'views/snippets/s_subscribe_1.xml',
        'views/snippets/s_subscribe_2.xml',
        'views/snippets/s_subscribe_3.xml',
        'views/snippets/s_subscribe_4.xml',
        'views/snippets/s_team_1.xml',
        'views/snippets/s_team_2.xml',
        'views/snippets/s_team_3.xml',
        'views/snippets/s_team_4.xml',
        'views/snippets/s_team_5.xml',
        'views/snippets/s_testimonial_1.xml',
        'views/snippets/s_testimonial_2.xml',
        'views/snippets/s_testimonial_3.xml',
        'views/snippets/s_testimonial_4.xml',
        'views/snippets/s_testimonial_5.xml',
        'views/snippets/s_video_1.xml',
        'views/snippets/s_google_map_1.xml',
        # Megamenu Snippets
        'views/snippets/s_mega_menu_1.xml',
        'views/snippets/s_mega_menu_2.xml',
        'views/snippets/s_mega_menu_3.xml',
        'views/snippets/s_mega_menu_4.xml',
        'views/snippets/s_mega_menu_5.xml',
        'views/snippets/s_mega_menu_6.xml',
        'views/snippets/s_mega_menu_7.xml',
        'views/snippets/s_mega_menu_8.xml',
        'views/snippets/s_mega_menu_9.xml',
        # Dynamic Snippets
        'views/dynamic_snippets/ecommerce_snippets.xml',
        'views/dynamic_snippets/mega_menu_snippets.xml',
    ],


}

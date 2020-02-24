from ykbl.setul import SetulShp

kolibäl = {
    '701': {'Kaqchikel': "Tz'olöj Ya'", 'español': 'Sololá'},
    '702': {'Kaqchikel': "Chaqaya'", 'español': 'San José Chacayá'},
    '703': {'Kaqchikel': "", 'español': 'Santa María Visitación'},
    '704': {'Kaqchikel': "", 'español': 'Santa Lucia Utatlán'},
    '705': {'Kaqchikel': "", 'español': 'Nahualá'},
    '706': {'Kaqchikel': "", 'español': 'Santa Catalina Ixtahuacán'},
    '707': {'Kaqchikel': "", 'español': 'Santa Clara La Laguna'},
    '708': {'Kaqchikel': "", 'español': 'Concepción'},
    '709': {'Kaqchikel': "Semetab'äj", 'español': 'San Andres Semetabaj'},
    '710': {'Kaqchikel': "Pan Ajache'l", 'español': 'Panajachel'},
    '711': {'Kaqchikel': "Kata'l Po'j", 'español': 'Santa Catarina Palopó'},
    '712': {'Kaqchikel': "Antun Po'j", 'español': 'San Antonio Palopó'},
    '713': {'Kaqchikel': "Loya'", 'español': 'San Lucas Tolimán'},
    '714': {'Kaqchikel': "", 'español': 'Santa Cruz La Laguna'},
    '715': {'Kaqchikel': "", 'español': 'San Pablo La Laguna', "Tz'utujil": "To k'or juyu'"},
    '716': {'Kaqchikel': "", 'español': 'San Marcos La Laguna'},
    '717': {'Kaqchikel': "Xe' Kuku' Ab'äj", 'español': 'San Juan La Laguna', "Tz'utujil": "Xe' Kuku' Aab'aj"},
    '718': {'Kaqchikel': "Tzunun Ya'", 'español': 'San Pedro La Laguna'},
    '719': {'Kaqchikel': "Tz'ikinajay", 'español': 'Santiago Atitlán'}
}

Tinamït = SetulShp(
    'Tinamït',
    'setul/muni y departamentos_gtm_fin/municipios_gtm_fin.shp',
    rucheel_etal='COD_MUNI',
    kolibäl=kolibäl
)

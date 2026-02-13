import json
import os
ARCHIVO_DB = "animales.json"
datos_iniciales = {
    "pregunta": "¿En qué medio vive principalmente?",
    "opciones": {
        "terrestre": {
            "pregunta": "¿Cuál es su hábitat específico?",
            "opciones": {
                "desierto": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene jorobas para almacenar grasa": {"animal": "Camello"},
                                        "No coincide con estas opciones": {"animal": "Coyote"}
                                    }
                                },
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un lagarto que parece tener collar": {"animal": "Lagarto de collar"},
                                        "No coincide con estas opciones": {"animal": "Monstruo de Gila"}
                                    }
                                },
                                "piel lisa y húmeda": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un sapo que se entierra en la arena": {"animal": "Sapo de espuelas"},
                                        "No coincide con estas opciones": {"animal": "Anfibio del desierto"}
                                    }
                                }
                            }
                        },
                        "0": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene un cascabel en la cola": {"animal": "Serpiente de cascabel"},
                                        "No coincide con estas opciones": {"animal": "Cobra de arena"}
                                    }
                                }
                            }
                        }
                    }
                },
                "selva": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un felino con manchas": {"animal": "Jaguar"},
                                        "No coincide con estas opciones": {"animal": "Gorila"}
                                    }
                                },
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es una iguana verde grande": {"animal": "Iguana"},
                                        "No coincide con estas opciones": {"animal": "Lagarto arborícola"}
                                    }
                                },
                                "piel lisa y húmeda": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es una rana pequeña de colores brillantes y venenosa": {"animal": "Rana dardo"},
                                        "No coincide con estas opciones": {"animal": "Rana de ojos rojos"}
                                    }
                                }
                            }
                        },
                        "0": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es una serpiente gigante que asfixia": {"animal": "Anaconda"},
                                        "No coincide con estas opciones": {"animal": "Boa constrictora"}
                                    }
                                }
                            }
                        }
                    }
                },
                "sabana": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene melena y ruge": {"animal": "León"},
                                        "No coincide con estas opciones": {"animal": "Guepardo"}
                                    }
                                },
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un lagarto monitor grande": {"animal": "Varano"},
                                        "No coincide con estas opciones": {"animal": "Lagarto de lengua azul"}
                                    }
                                },
                                "piel lisa y húmeda": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un sapo africano gigante": {"animal": "Sapo buey"},
                                        "No coincide con estas opciones": {"animal": "Rana de lluvia"}
                                    }
                                }
                            }
                        },
                        "0": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es la serpiente más rápida y agresiva": {"animal": "Mamba Negra"},
                                        "No coincide con estas opciones": {"animal": "Pitón de roca"}
                                    }
                                }
                            }
                        }
                    }
                },
                "polo": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje grueso": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un oso blanco gigante": {"animal": "Oso Polar"},
                                        "No coincide con estas opciones": {"animal": "Zorro Ártico"}
                                    }
                                }
                            }
                        },
                        "2": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "plumas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es un ave que no vuela y nada muy bien": {"animal": "Pingüino"},
                                        "No coincide con estas opciones": {"animal": "Búho Nival"}
                                    }
                                }
                            }
                        },
                        "0": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "piel gruesa y grasosa": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene colmillos y vive en el agua fría": {"animal": "Morsa"},
                                        "No coincide con estas opciones": {"animal": "Ballena de Groenlandia"}
                                    }
                                }
                            }
                        }
                    }
                },
                "granja": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Produce lana": {"animal": "Oveja"},
                                        "No coincide con estas opciones": {"animal": "Vaca"}
                                    }
                                },
                                "piel gruesa con cerdas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Le gusta el lodo y tiene nariz de enchufe": {"animal": "Cerdo"},
                                        "No coincide con estas opciones": {"animal": "Burro"}
                                    }
                                }
                            }
                        },
                        "2": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "plumas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene cresta y pone huevos": {"animal": "Gallina"},
                                        "No coincide con estas opciones": {"animal": "Pato"}
                                    }
                                }
                            }
                        }
                    }
                },
                "casa (mascota)": {
                    "pregunta": "¿Cuántas patas tiene?",
                    "opciones": {
                        "4": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "pelaje": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es el mejor amigo del hombre": {"animal": "Perro"},
                                        "No coincide con estas opciones": {"animal": "Gato"}
                                    }
                                }
                            }
                        },
                        "2": {
                            "pregunta": "¿Cuál de estas características describe mejor al animal?",
                            "opciones": {
                                "Canta y puede imitar sonidos": {"animal": "Loro"},
                                "No coincide con estas opciones": {"animal": "Canario"}
                            }
                        },
                        "0": {
                            "pregunta": "¿Cuál de estas características describe mejor al animal?",
                            "opciones": {
                                "Vive en un acuario y tiene escamas": {"animal": "Pez de acuario"},
                                "No coincide con estas opciones": {"animal": "Ajolote"}
                            }
                        }
                    }
                }
            }
        },
        "acuatico": {
            "pregunta": "¿Qué tipo de agua prefiere?",
            "opciones": {
                "salada": {
                    "pregunta": "¿Cómo respira?",
                    "opciones": {
                        "pulmones": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "piel lisa": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Es muy inteligente y salta": {"animal": "Delfín"},
                                        "No coincide con estas opciones": {"animal": "Ballena azul"}
                                    }
                                }
                            }
                        },
                        "branquias": {
                            "pregunta": "¿Cómo está cubierta su piel?",
                            "opciones": {
                                "escamas": {
                                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                                    "opciones": {
                                        "Tiene dientes de sierra y es un depredador": {"animal": "Tiburón"},
                                        "No coincide con estas opciones": {"animal": "Pez Payaso"}
                                    }
                                }
                            }
                        }
                    }
                },
                "dulce": {
                    "pregunta": "¿Cómo está cubierta su piel?",
                    "opciones": {
                        "escamas": {
                            "pregunta": "¿Cuál de estas características describe mejor al animal?",
                            "opciones": {
                                "Tiene una aleta adiposa": {"animal": "Trucha"},
                                "No coincide con estas opciones": {"animal": "Piraña"}
                            }
                        }
                    }
                }
            }
        },
        "volador": {
            "pregunta": "¿Qué tipo de especie es?",
            "opciones": {
                "aves": {
                    "pregunta": "¿Qué tipo de alimentación tiene?",
                    "opciones": {
                        "rapaz (carnívoro)": {
                            "pregunta": "¿Cuál de estas características describe mejor al animal?",
                            "opciones": {
                                "Tiene una vista asombrosa y garras": {"animal": "Águila"},
                                "No coincide con estas opciones": {"animal": "Halcón"}
                            }
                        },
                        "granívoro (semillas)": {
                            "pregunta": "¿Cuál de estas características describe mejor al animal?",
                            "opciones": {
                                "Succiona el agua al beber": {"animal": "Paloma"},
                                "No coincide con estas opciones": {"animal": "Gorrión"}
                            }
                        }
                    }
                },
                "insectos": {
                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                    "opciones": {
                        "Tiene alas de colores y poliniza flores": {"animal": "Mariposa"},
                        "No coincide con estas opciones": {"animal": "Abeja"}
                    }
                },
                "mamíferos": {
                    "pregunta": "¿Cuál de estas características describe mejor al animal?",
                    "opciones": {
                        "Vuela de noche usando ecolocalización": {"animal": "Murciélago"},
                        "No coincide con estas opciones": {"animal": "Zorro volador"}
                    }
                }
            }
        }
    }
}
#//////////////////////////////////////////////////////////////////////////////////#
def guardar_datos(datos):
    try:
        with open(ARCHIVO_DB, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("¡Conocimiento guardado! ✅")
    except:
        print("Error al guardar.")

def cargar_y_jugar():
    datos = datos_iniciales
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except: pass

    nodo = datos
    print("🐾 IA ADIVINADORA DE ANIMALES 🐾\nPiensa en un animal...")

    while True:
        pregunta = nodo.get("pregunta", "Elige una opción:")
        opciones = nodo.get("opciones", {})
        es_nivel_final = any("animal" in v and "opciones" not in v for v in opciones.values())
        clave_escape = "No coincide con estas opciones"

        print(f"\n{pregunta}")
        
        if es_nivel_final:
            lista_claves = [k for k in opciones.keys() if k != clave_escape]
            for i, op in enumerate(lista_claves, 1):
                print(f"{i}. {op}")
            idx_escape = len(lista_claves) + 1
            print(f"{idx_escape}. {clave_escape}")
        else:
            lista_claves = list(opciones.keys())
            for i, op in enumerate(lista_claves, 1):
                print(f"{i}. {op}")
            idx_escape = -1 

        try:
            seleccion = int(input("Elige un número: "))
            if es_nivel_final and seleccion == idx_escape:
                animal_fallback = opciones[clave_escape]["animal"]
                print(f"\n¿Estás pensando en un(a) {animal_fallback.upper()}?")
                if input("1. Sí / 2. No: ") == "1":
                    print(f"¡Genial! Sabía que era el {animal_fallback}. 🎉")
                else:
                    print(f"\n¡Me has ganado! No es el {animal_fallback}.")
                    nuevo = input("¿Cuál era el animal?: ").strip()
                    char = input(f"¿Qué característica distingue al {nuevo}?: ").strip()
                    opciones[char] = {"animal": nuevo}
                    guardar_datos(datos)
                    print(f"Gracias, ahora sé que el {nuevo} se distingue por: {char}.")
                return
            clave_elegida = lista_claves[seleccion - 1]
            nodo = opciones[clave_elegida]
            if "animal" in nodo and "opciones" not in nodo:
                print(f"\n¿Estás pensando en un(a) {nodo['animal'].upper()}?")
                if input("1. Sí / 2. No: ") == "1":
                    print(f"¡Genial! Sabía que era el {nodo['animal']}. 🎉")
                else:
                    print("¡Vaya! Me has ganado esta vez.")
                return
        except (ValueError, IndexError):
            print("Selección no válida. Intenta de nuevo.")
if __name__ == "__main__":
    cargar_y_jugar()
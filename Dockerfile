FROM quay.io/numigi/odoo-public:12.latest
MAINTAINER numigi <contact@numigi.com>

USER root

COPY .docker_files/test-requirements.txt .
RUN pip3 install -r test-requirements.txt

ENV THIRD_PARTY_ADDONS /mnt/third-party-addons
RUN mkdir -p "${THIRD_PARTY_ADDONS}" && chown -R odoo "${THIRD_PARTY_ADDONS}"
COPY ./gitoo.yml /gitoo.yml
RUN gitoo install-all --conf_file /gitoo.yml --destination "${THIRD_PARTY_ADDONS}"

USER odoo

COPY hr_contract_single_open /mnt/extra-addons/hr_contract_single_open
COPY hr_contract_wage_type /mnt/extra-addons/hr_contract_wage_type
COPY hr_employee_private_wizard /mnt/extra-addons/hr_employee_private_wizard
COPY hr_employee_type /mnt/extra-addons/hr_employee_type
COPY hr_employee_type_private_wizard /mnt/extra-addons/hr_employee_type_private_wizard
COPY hr_event /mnt/extra-addons/hr_event
COPY hr_expense_same_month /mnt/extra-addons/hr_expense_same_month
COPY hr_working_space /mnt/extra-addons/hr_working_space

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo

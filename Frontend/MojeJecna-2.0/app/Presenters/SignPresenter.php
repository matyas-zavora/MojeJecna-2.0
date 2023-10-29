<?php
namespace App\Presenters;

use Nette;
use Nette\Application\UI\Form;
use App\Models\ApiModel;
use Nette\Application\UI\Presenter;

final class SignPresenter extends Presenter
{
    private $apiModel;

    public function __construct(ApiModel $apiModel)
    {
        parent::__construct();
        $this->apiModel = $apiModel;
    }

    protected function createComponentSignInForm(): Form
    {
        $form = new Form;
        $form->addText('username', 'Uživatelské jméno:')
            ->setRequired('Prosím vyplňte své uživatelské jméno.');

        $form->addPassword('password', 'Heslo:')
            ->setRequired('Prosím vyplňte své heslo.');

        $form->addSubmit('send', 'Přihlásit');

        $form->onSuccess[] = $this->signInFormSucceeded(...);
        return $form;
    }

    private function signInFormSucceeded(Form $form, \stdClass $data): void
    {
        $response = $this->apiModel->login($data->username, $data->password);
        if($response->status === 'success'){
            $this->redirect('Home:');
        } else {
            $form->addError('Přihlášení se nezdařilo. Zkuste to prosím znovu.');
        }
    }

    public function actionOut(): void
    {
        $this->getUser()->logout();
        $this->flashMessage('Odhlášení bylo úspěšné.');
        $this->redirect('Home:');
    }
}
